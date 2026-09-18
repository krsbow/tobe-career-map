import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { CAREERS, Career } from '../data/careersData';
import { useAuth } from './AuthContext';
import { supabase, isSupabaseConfigured } from '../lib/supabase';

export interface MilestoneTask {
  id: string;
  text: string;
  completed: boolean;
}

export interface RoadmapMilestone {
  id: string;
  phase: string;
  title: string;
  category: 'Foundation' | 'Skills' | 'Portfolio' | 'Career Launch';
  status: 'done' | 'active' | 'upcoming';
  estimatedWeeks: string;
  description: string;
  tasks: MilestoneTask[];
}

export interface ActiveRoadmap {
  id?: string;
  careerId: string;
  careerTitle: string;
  createdAt: string;
  milestones: RoadmapMilestone[];
  notes: string;
}

export interface CareerNote {
  id: string;
  careerId?: string;
  careerTitle?: string;
  title?: string;
  content: string;
  createdAt: string;
}

export interface AssessmentResult {
  completedAt: string;
  riasecScores: Record<string, number>;
  topTraits: string[];
  selectedSkills: string[];
  matchedCareers: {
    careerId: string;
    matchScore: number;
    breakdown: {
      interests: number;
      skills: number;
    };
  }[];
}

interface UserIsolatedData {
  savedCareerIds: string[];
  recentlyViewed: { careerId: string; viewedAt: string }[];
  assessmentResults: AssessmentResult | null;
  roadmaps: ActiveRoadmap[];
  activeRoadmapId: string | null;
  activeRoadmap?: ActiveRoadmap | null; // For backward compatibility
  careerNotes: CareerNote[];
}

interface CareerContextType {
  careers: Career[];
  savedCareerIds: string[];
  recentlyViewed: { careerId: string; viewedAt: string }[];
  assessmentResults: AssessmentResult | null;
  roadmaps: ActiveRoadmap[];
  activeRoadmapId: string | null;
  activeRoadmap: ActiveRoadmap | null;
  careerNotes: CareerNote[];
  toggleSaveCareer: (careerId: string) => Promise<void>;
  isCareerSaved: (careerId: string) => boolean;
  recordView: (careerId: string) => Promise<void>;
  saveAssessment: (results: AssessmentResult) => Promise<void>;
  clearAssessment: () => Promise<void>;
  createOrSetRoadmap: (careerId: string) => Promise<void>;
  switchActiveRoadmap: (careerId: string) => Promise<void>;
  deleteRoadmap: (careerId: string) => Promise<void>;
  toggleRoadmapTask: (milestoneId: string, taskId: string) => Promise<void>;
  setMilestoneStatus: (milestoneId: string, status: 'done' | 'active' | 'upcoming') => Promise<void>;
  updateRoadmapNotes: (notes: string) => Promise<void>;
  addCareerNote: (content: string, title?: string, careerId?: string, careerTitle?: string) => Promise<void>;
  deleteCareerNote: (noteId: string) => Promise<void>;
  clearRoadmap: () => Promise<void>;
  calculateCareerMatch: (career: Career) => number;
}

const CareerContext = createContext<CareerContextType | undefined>(undefined);

export function CareerProvider({ children }: { children: ReactNode }) {
  const { user } = useAuth();

  const [savedCareerIds, setSavedCareerIds] = useState<string[]>([]);
  const [recentlyViewed, setRecentlyViewed] = useState<{ careerId: string; viewedAt: string }[]>([]);
  const [assessmentResults, setAssessmentResults] = useState<AssessmentResult | null>(null);
  const [roadmaps, setRoadmaps] = useState<ActiveRoadmap[]>([]);
  const [activeRoadmapId, setActiveRoadmapId] = useState<string | null>(null);
  const [careerNotes, setCareerNotes] = useState<CareerNote[]>([]);

  // Derived active roadmap object
  const activeRoadmap: ActiveRoadmap | null =
    roadmaps.find((r) => r.careerId === activeRoadmapId || r.id === activeRoadmapId) ||
    (roadmaps.length > 0 ? roadmaps[0] : null);

  // When user changes (login, logout, switch account), load ONLY that user's isolated data
  useEffect(() => {
    if (!user) {
      // User logged out: Completely clear all in-memory user data
      setSavedCareerIds([]);
      setRecentlyViewed([]);
      setAssessmentResults(null);
      setRoadmaps([]);
      setActiveRoadmapId(null);
      setCareerNotes([]);
      return;
    }

    const userId = user.id;

    async function loadUserData() {
      if (isSupabaseConfigured) {
        try {
          // 1. Fetch saved careers protected by RLS
          const { data: savedData } = await supabase
            .from('saved_careers')
            .select('career_id')
            .eq('user_id', userId);
          if (savedData) {
            setSavedCareerIds(savedData.map((r) => r.career_id));
          }

          // 2. Fetch recently viewed protected by RLS
          const { data: viewedData } = await supabase
            .from('recent_views')
            .select('career_id, viewed_at')
            .eq('user_id', userId)
            .order('viewed_at', { ascending: false })
            .limit(10);
          if (viewedData) {
            setRecentlyViewed(
              viewedData.map((r) => ({
                careerId: r.career_id,
                viewedAt: r.viewed_at,
              }))
            );
          }

          // 3. Fetch latest assessment results protected by RLS
          const { data: assessData } = await supabase
            .from('assessments')
            .select('*')
            .eq('user_id', userId)
            .order('created_at', { ascending: false })
            .limit(1)
            .maybeSingle();

          if (assessData) {
            const { data: matchData } = await supabase
              .from('career_matches')
              .select('*')
              .eq('user_id', userId);

            setAssessmentResults({
              completedAt: assessData.created_at,
              riasecScores: assessData.riasec_scores || {},
              topTraits: assessData.top_traits || [],
              selectedSkills: assessData.selected_skills || [],
              matchedCareers: (matchData || []).map((m) => ({
                careerId: m.career_id,
                matchScore: m.match_score,
                breakdown: m.breakdown || { interests: 0, skills: 0 },
              })),
            });
          } else {
            setAssessmentResults(null);
          }

          // 4. Fetch all user roadmaps & milestones protected by RLS
          const { data: allRoadmapsData } = await supabase
            .from('roadmaps')
            .select('*')
            .eq('user_id', userId)
            .order('created_at', { ascending: false });

          if (allRoadmapsData && allRoadmapsData.length > 0) {
            const loadedRoadmaps: ActiveRoadmap[] = [];
            for (const rm of allRoadmapsData) {
              const { data: milestoneData } = await supabase
                .from('roadmap_milestones')
                .select('*')
                .eq('roadmap_id', rm.id)
                .order('created_at', { ascending: true });

              loadedRoadmaps.push({
                id: rm.id,
                careerId: rm.career_id,
                careerTitle: rm.career_title,
                createdAt: new Date(rm.created_at).toLocaleDateString('en-US', {
                  month: 'short',
                  day: 'numeric',
                  year: 'numeric',
                }),
                notes: rm.notes || '',
                milestones: (milestoneData || []).map((m) => ({
                  id: m.id,
                  phase: m.phase,
                  title: m.title,
                  category: m.category,
                  status: m.status,
                  estimatedWeeks: m.estimated_weeks,
                  description: m.description,
                  tasks: m.tasks || [],
                })),
              });
            }

            setRoadmaps(loadedRoadmaps);
            const activeRm = allRoadmapsData.find((r) => r.status === 'active') || allRoadmapsData[0];
            setActiveRoadmapId(activeRm ? activeRm.career_id : loadedRoadmaps[0].careerId);
          } else {
            setRoadmaps([]);
            setActiveRoadmapId(null);
          }

          // 5. Fetch career notes protected by RLS
          const { data: notesData } = await supabase
            .from('career_notes')
            .select('*')
            .eq('user_id', userId)
            .order('created_at', { ascending: false });

          if (notesData) {
            setCareerNotes(
              notesData.map((n) => ({
                id: n.id,
                careerId: n.career_id,
                careerTitle: n.career_title,
                title: n.title,
                content: n.content,
                createdAt: new Date(n.created_at).toLocaleDateString('en-US', {
                  month: 'short',
                  day: 'numeric',
                  year: 'numeric',
                  hour: 'numeric',
                  minute: '2-digit',
                }),
              }))
            );
          } else {
            setCareerNotes([]);
          }
          return;
        } catch (err) {
          console.warn('Supabase data load error:', err);
        }
      }

      // Local isolated storage partition strictly keyed by user.id
      const storageKey = `tobe_userdata_${userId}`;
      const localDataRaw = localStorage.getItem(storageKey);
      if (localDataRaw) {
        try {
          const parsed: UserIsolatedData = JSON.parse(localDataRaw);
          setSavedCareerIds(parsed.savedCareerIds || []);
          setRecentlyViewed(parsed.recentlyViewed || []);
          setAssessmentResults(parsed.assessmentResults || null);

          // Handle backward compatibility if parsed.roadmaps vs parsed.activeRoadmap
          let rList: ActiveRoadmap[] = parsed.roadmaps || [];
          if (rList.length === 0 && parsed.activeRoadmap) {
            rList = [parsed.activeRoadmap];
          }
          setRoadmaps(rList);
          setActiveRoadmapId(parsed.activeRoadmapId || (rList.length > 0 ? rList[0].careerId : null));
          setCareerNotes(parsed.careerNotes || []);
        } catch {
          setSavedCareerIds([]);
          setRecentlyViewed([]);
          setAssessmentResults(null);
          setRoadmaps([]);
          setActiveRoadmapId(null);
          setCareerNotes([]);
        }
      } else {
        // First-time user gets clean empty state
        setSavedCareerIds([]);
        setRecentlyViewed([]);
        setAssessmentResults(null);
        setRoadmaps([]);
        setActiveRoadmapId(null);
        setCareerNotes([]);
      }
    }

    loadUserData();
  }, [user?.id]);

  // Helper to persist user-scoped local fallback
  const syncLocalBackup = (updated: Partial<UserIsolatedData>) => {
    if (!user) return;
    const storageKey = `tobe_userdata_${user.id}`;
    const current: UserIsolatedData = {
      savedCareerIds,
      recentlyViewed,
      assessmentResults,
      roadmaps,
      activeRoadmapId,
      careerNotes,
      ...updated,
    };
    localStorage.setItem(storageKey, JSON.stringify(current));
  };

  const toggleSaveCareer = async (careerId: string) => {
    if (!user) return;
    const isSaved = savedCareerIds.includes(careerId);
    const nextSaved = isSaved
      ? savedCareerIds.filter((id) => id !== careerId)
      : [...savedCareerIds, careerId];

    setSavedCareerIds(nextSaved);
    syncLocalBackup({ savedCareerIds: nextSaved });

    if (isSupabaseConfigured) {
      try {
        if (isSaved) {
          await supabase.from('saved_careers').delete().eq('user_id', user.id).eq('career_id', careerId);
        } else {
          await supabase.from('saved_careers').insert({ user_id: user.id, career_id: careerId });
        }
      } catch (err) {
        console.warn('Error syncing saved_careers to Supabase:', err);
      }
    }
  };

  const isCareerSaved = (careerId: string) => savedCareerIds.includes(careerId);

  const recordView = async (careerId: string) => {
    if (!user) return;
    const now = new Date().toISOString();
    const filtered = recentlyViewed.filter((item) => item.careerId !== careerId);
    const updated = [{ careerId, viewedAt: now }, ...filtered].slice(0, 10);

    setRecentlyViewed(updated);
    syncLocalBackup({ recentlyViewed: updated });

    if (isSupabaseConfigured) {
      try {
        await supabase.from('recent_views').upsert(
          {
            user_id: user.id,
            career_id: careerId,
            viewed_at: now,
          },
          { onConflict: 'user_id,career_id' }
        );
      } catch (err) {
        console.warn('Error syncing recent_views to Supabase:', err);
      }
    }
  };

  const saveAssessment = async (results: AssessmentResult) => {
    if (!user) return;
    setAssessmentResults(results);
    syncLocalBackup({ assessmentResults: results });

    if (isSupabaseConfigured) {
      try {
        const { data: assessRecord } = await supabase
          .from('assessments')
          .insert({
            user_id: user.id,
            riasec_scores: results.riasecScores,
            top_traits: results.topTraits,
            selected_skills: results.selectedSkills,
          })
          .select()
          .single();

        if (assessRecord && results.matchedCareers?.length > 0) {
          const matchPayload = results.matchedCareers.map((m) => ({
            assessment_id: assessRecord.id,
            user_id: user.id,
            career_id: m.careerId,
            match_score: m.matchScore,
            breakdown: m.breakdown,
          }));
          await supabase.from('career_matches').insert(matchPayload);
        }
      } catch (err) {
        console.warn('Error saving assessment to Supabase:', err);
      }
    }
  };

  const clearAssessment = async () => {
    if (!user) return;
    setAssessmentResults(null);
    syncLocalBackup({ assessmentResults: null });

    if (isSupabaseConfigured) {
      try {
        await supabase.from('assessments').delete().eq('user_id', user.id);
        await supabase.from('career_matches').delete().eq('user_id', user.id);
      } catch (err) {
        console.warn('Error clearing assessment from Supabase:', err);
      }
    }
  };

  const switchActiveRoadmap = async (careerId: string) => {
    if (!user) return;
    setActiveRoadmapId(careerId);
    syncLocalBackup({ activeRoadmapId: careerId });

    if (isSupabaseConfigured) {
      try {
        await supabase.from('roadmaps').update({ status: 'saved' }).eq('user_id', user.id);
        await supabase.from('roadmaps').update({ status: 'active' }).eq('user_id', user.id).eq('career_id', careerId);
      } catch (err) {
        console.warn('Error switching active roadmap in Supabase:', err);
      }
    }
  };

  const createOrSetRoadmap = async (careerId: string) => {
    if (!user) return;
    const career = CAREERS.find((c) => c.id === careerId);
    if (!career) return;

    // Check if roadmap already exists for this career
    const existingIndex = roadmaps.findIndex((r) => r.careerId === careerId);
    if (existingIndex >= 0) {
      // Simply switch active focus to this existing roadmap without resetting its tasks
      await switchActiveRoadmap(careerId);
      return;
    }

    const newMilestones: RoadmapMilestone[] = [
      {
        id: 'm1_' + Date.now(),
        phase: 'Phase 1: Foundations & Core Concepts',
        title: `Master ${career.title} Fundamentals`,
        category: 'Foundation',
        status: 'active',
        estimatedWeeks: 'Weeks 1�4',
        description: `Build a rock-solid mental model and essential skills for ${career.title}.`,
        tasks: [
          { id: 't1_1', text: `Learn core prerequisite skills: ${career.core_skills.slice(0, 3).join(', ')}`, completed: false },
          { id: 't1_2', text: `Set up professional development tools: ${career.common_tools.slice(0, 3).join(', ')}`, completed: false },
          { id: 't1_3', text: `Complete foundational learning path: ${career.learning_resources[0]?.title || 'Introductory Documentation'}`, completed: false },
        ],
      },
      {
        id: 'm2_' + Date.now(),
        phase: 'Phase 2: Applied Competence & Practical Projects',
        title: 'Build Real-World Project Demonstrations',
        category: 'Skills',
        status: 'upcoming',
        estimatedWeeks: 'Weeks 5�10',
        description: `Apply theoretical knowledge by building authentic portfolio items.`,
        tasks: [
          { id: 't2_1', text: `Construct Project 1: ${career.portfolio_projects[0]?.title || 'Starter Prototype'}`, completed: false },
          { id: 't2_2', text: `Expand skillset to include: ${career.optional_skills.slice(0, 3).join(', ')}`, completed: false },
          { id: 't2_3', text: `Build Intermediate Capstone: ${career.portfolio_projects[1]?.title || 'Full Project'}`, completed: false },
        ],
      },
      {
        id: 'm3_' + Date.now(),
        phase: 'Phase 3: Portfolio & Industry Credentialing',
        title: 'Certifications and Portfolio Polish',
        category: 'Portfolio',
        status: 'upcoming',
        estimatedWeeks: 'Weeks 11�16',
        description: `Validate your expertise with recognized credentials and a publicly verifiable showcase.`,
        tasks: [
          { id: 't3_1', text: `Earn credential: ${career.certifications[0]?.name || 'Professional Certificate'}`, completed: false },
          { id: 't3_2', text: `Build Advanced Capstone: ${career.portfolio_projects[2]?.title || 'Production System'}`, completed: false },
          { id: 't3_3', text: 'Document architecture, design decisions, and write a technical case study', completed: false },
        ],
      },
      {
        id: 'm4_' + Date.now(),
        phase: 'Phase 4: Career Launch & Interview Readiness',
        title: 'Market Positioning and Job Applications',
        category: 'Career Launch',
        status: 'upcoming',
        estimatedWeeks: 'Weeks 17�20',
        description: `Position yourself for roles with targeted salary benchmarks in the Philippines (${career.salary_data.philippines.entry_level.split('(')[0]}) or Global Remote.`,
        tasks: [
          { id: 't4_1', text: 'Polish resume and LinkedIn / GitHub / Figma portfolio links', completed: false },
          { id: 't4_2', text: 'Conduct mock interviews covering technical and behavioral questions', completed: false },
          { id: 't4_3', text: 'Apply to curated entry-level or junior opportunities and track outcomes', completed: false },
        ],
      },
    ];

    const newRoadmap: ActiveRoadmap = {
      careerId: career.id,
      careerTitle: career.title,
      createdAt: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      milestones: newMilestones,
      notes: '',
    };

    const nextRoadmaps = [newRoadmap, ...roadmaps];
    setRoadmaps(nextRoadmaps);
    setActiveRoadmapId(career.id);
    syncLocalBackup({ roadmaps: nextRoadmaps, activeRoadmapId: career.id });

    if (isSupabaseConfigured) {
      try {
        // Set previous roadmaps to 'saved'
        await supabase.from('roadmaps').update({ status: 'saved' }).eq('user_id', user.id);

        // Create new roadmap record
        const { data: rm } = await supabase
          .from('roadmaps')
          .insert({
            user_id: user.id,
            career_id: career.id,
            career_title: career.title,
            status: 'active',
          })
          .select()
          .single();

        if (rm) {
          const milestonesPayload = newMilestones.map((m) => ({
            roadmap_id: rm.id,
            phase: m.phase,
            title: m.title,
            category: m.category,
            status: m.status,
            estimated_weeks: m.estimatedWeeks,
            description: m.description,
            tasks: m.tasks,
          }));
          await supabase.from('roadmap_milestones').insert(milestonesPayload);
          newRoadmap.id = rm.id;
          setRoadmaps((prev) => prev.map((r) => (r.careerId === career.id ? { ...r, id: rm.id } : r)));
        }
      } catch (err) {
        console.warn('Error syncing roadmap to Supabase:', err);
      }
    }
  };

  const deleteRoadmap = async (careerId: string) => {
    if (!user) return;
    const target = roadmaps.find((r) => r.careerId === careerId || r.id === careerId);
    const nextRoadmaps = roadmaps.filter((r) => r.careerId !== careerId && r.id !== careerId);
    setRoadmaps(nextRoadmaps);

    const nextActiveId = nextRoadmaps.length > 0 ? nextRoadmaps[0].careerId : null;
    setActiveRoadmapId(nextActiveId);
    syncLocalBackup({ roadmaps: nextRoadmaps, activeRoadmapId: nextActiveId });

    if (isSupabaseConfigured && target?.id) {
      try {
        await supabase.from('roadmaps').delete().eq('user_id', user.id).eq('id', target.id);
      } catch (err) {
        console.warn('Error deleting roadmap from Supabase:', err);
      }
    }
  };

  const toggleRoadmapTask = async (milestoneId: string, taskId: string) => {
    if (!activeRoadmap || !user) return;
    const updatedMilestones = activeRoadmap.milestones.map((m) => {
      if (m.id !== milestoneId) return m;
      const updatedTasks = m.tasks.map((t) => (t.id === taskId ? { ...t, completed: !t.completed } : t));
      const allDone = updatedTasks.every((t) => t.completed);
      const someDone = updatedTasks.some((t) => t.completed);
      let status = m.status;
      if (allDone) status = 'done';
      else if (someDone && m.status === 'upcoming') status = 'active';
      return { ...m, tasks: updatedTasks, status };
    });

    const updatedRoadmap = { ...activeRoadmap, milestones: updatedMilestones };
    const nextRoadmaps = roadmaps.map((r) => (r.careerId === activeRoadmap.careerId ? updatedRoadmap : r));
    setRoadmaps(nextRoadmaps);
    syncLocalBackup({ roadmaps: nextRoadmaps });

    if (isSupabaseConfigured && activeRoadmap.id) {
      try {
        const targetMilestone = updatedMilestones.find((m) => m.id === milestoneId);
        if (targetMilestone) {
          await supabase
            .from('roadmap_milestones')
            .update({ tasks: targetMilestone.tasks, status: targetMilestone.status })
            .eq('id', milestoneId);
        }
      } catch (err) {
        console.warn('Error updating milestone tasks in Supabase:', err);
      }
    }
  };

  const setMilestoneStatus = async (milestoneId: string, status: 'done' | 'active' | 'upcoming') => {
    if (!activeRoadmap || !user) return;
    const updatedMilestones = activeRoadmap.milestones.map((m) => {
      if (m.id !== milestoneId) return m;
      const tasks = m.tasks.map((t) => ({ ...t, completed: status === 'done' }));
      return { ...m, status, tasks };
    });

    const updatedRoadmap = { ...activeRoadmap, milestones: updatedMilestones };
    const nextRoadmaps = roadmaps.map((r) => (r.careerId === activeRoadmap.careerId ? updatedRoadmap : r));
    setRoadmaps(nextRoadmaps);
    syncLocalBackup({ roadmaps: nextRoadmaps });

    if (isSupabaseConfigured && activeRoadmap.id) {
      try {
        await supabase
          .from('roadmap_milestones')
          .update({ status })
          .eq('id', milestoneId);
      } catch (err) {
        console.warn('Error updating milestone status in Supabase:', err);
      }
    }
  };

  const updateRoadmapNotes = async (notes: string) => {
    if (!activeRoadmap || !user) return;
    const updatedRoadmap = { ...activeRoadmap, notes };
    const nextRoadmaps = roadmaps.map((r) => (r.careerId === activeRoadmap.careerId ? updatedRoadmap : r));
    setRoadmaps(nextRoadmaps);
    syncLocalBackup({ roadmaps: nextRoadmaps });

    if (isSupabaseConfigured && activeRoadmap.id) {
      try {
        await supabase.from('roadmaps').update({ notes }).eq('id', activeRoadmap.id);
      } catch (err) {
        console.warn('Error updating roadmap notes in Supabase:', err);
      }
    }
  };

  const addCareerNote = async (
    content: string,
    title?: string,
    careerId?: string,
    careerTitle?: string
  ) => {
    if (!content.trim() || !user) return;
    const newNote: CareerNote = {
      id: 'note_' + Date.now() + '_' + Math.random().toString(36).substring(2, 6),
      title: title?.trim() || undefined,
      content: content.trim(),
      careerId: careerId || activeRoadmap?.careerId,
      careerTitle: careerTitle || activeRoadmap?.careerTitle,
      createdAt: new Date().toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
      }),
    };

    const nextNotes = [newNote, ...careerNotes];
    setCareerNotes(nextNotes);
    syncLocalBackup({ careerNotes: nextNotes });

    if (isSupabaseConfigured) {
      try {
        await supabase.from('career_notes').insert({
          user_id: user.id,
          title: newNote.title,
          content: newNote.content,
          career_id: newNote.careerId,
          career_title: newNote.careerTitle,
        });
      } catch (err) {
        console.warn('Error adding note to Supabase:', err);
      }
    }
  };

  const deleteCareerNote = async (noteId: string) => {
    if (!user) return;
    const nextNotes = careerNotes.filter((n) => n.id !== noteId);
    setCareerNotes(nextNotes);
    syncLocalBackup({ careerNotes: nextNotes });

    if (isSupabaseConfigured) {
      try {
        await supabase.from('career_notes').delete().eq('user_id', user.id).eq('id', noteId);
      } catch (err) {
        console.warn('Error deleting note from Supabase:', err);
      }
    }
  };

  const clearRoadmap = async () => {
    if (!user || !activeRoadmap) return;
    await deleteRoadmap(activeRoadmap.careerId);
  };

  const calculateCareerMatch = (career: Career): number => {
    if (!assessmentResults) return 0;
    const match = assessmentResults.matchedCareers.find((m) => m.careerId === career.id);
    return match ? match.matchScore : 0;
  };

  return (
    <CareerContext.Provider
      value={{
        careers: CAREERS,
        savedCareerIds,
        recentlyViewed,
        assessmentResults,
        roadmaps,
        activeRoadmapId,
        activeRoadmap,
        careerNotes,
        toggleSaveCareer,
        isCareerSaved,
        recordView,
        saveAssessment,
        clearAssessment,
        createOrSetRoadmap,
        switchActiveRoadmap,
        deleteRoadmap,
        toggleRoadmapTask,
        setMilestoneStatus,
        updateRoadmapNotes,
        addCareerNote,
        deleteCareerNote,
        clearRoadmap,
        calculateCareerMatch,
      }}
    >
      {children}
    </CareerContext.Provider>
  );
}

export const useCareer = () => {
  const context = useContext(CareerContext);
  if (!context) {
    throw new Error('useCareer must be used within a CareerProvider');
  }
  return context;
};
