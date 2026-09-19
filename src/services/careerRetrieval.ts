/**
 * Career Knowledge Retrieval (RAG) Service for Frontend
 * Retrieves targeted career facts on demand matching user inquiries.
 */

import { CAREERS, Career } from '../data/careersData';

export class CareerRetrievalService {
  /**
   * Retrieve query-relevant facts from the career catalog.
   */
  retrieveRelevantFacts(query: string, careerTitleOrId?: string): string[] {
    if (!careerTitleOrId) return [];

    const q = query.toLowerCase();
    const facts: string[] = [];

    const career = CAREERS.find(
      (c) =>
        c.id.toLowerCase() === careerTitleOrId.toLowerCase() ||
        c.title.toLowerCase() === careerTitleOrId.toLowerCase()
    );

    if (!career) return [];

    const title = career.title;

    // 1. Design & Drawing inquiries
    if (q.includes('draw') || q.includes('drawing') || q.includes('art') || q.includes('sketch') || q.includes('design')) {
      if (title.toLowerCase().includes('design') || title.toLowerCase().includes('ux')) {
        facts.push(`${title} focuses on digital layout hierarchy, component structure, usability heuristics, and user flows in Figma; fine-art drawing or freehand sketching is not required.`);
      } else if (title.toLowerCase().includes('developer') || title.toLowerCase().includes('engineer')) {
        facts.push(`${title} emphasizes logic, architecture, and code; artistic drawing ability is completely unrelated.`);
      }
    }

    // 2. Math & Intelligence inquiries
    if (q.includes('math') || q.includes('smart') || q.includes('genius') || q.includes('calculus')) {
      if (title.toLowerCase().includes('developer') || title.toLowerCase().includes('software') || title.toLowerCase().includes('web')) {
        facts.push(`Standard software development relies on basic logic, arithmetic, and problem decomposition; calculus or advanced higher math is rarely needed for general web/app development.`);
      } else if (title.toLowerCase().includes('civil')) {
        facts.push(`${title} uses applied algebra, geometry, and structural mechanics, supported heavily by specialized CAD software.`);
      }
    }

    // 3. Education & Degree
    if (q.includes('degree') || q.includes('college') || q.includes('university') || q.includes('license') || q.includes('prc')) {
      if (['registered-nurse', 'civil-engineer', 'cpa-accountant'].includes(career.id)) {
        facts.push(`${title} is a legally regulated profession in the Philippines requiring a CHED-accredited bachelor's degree and passing the official PRC Board Examination.`);
      } else {
        facts.push(`In ${title}, proof of practical capability (real portfolio projects, GitHub code repositories, and problem-solving ability) is the primary hiring signal; a formal degree is rarely a strict blocker.`);
      }
    }

    // 4. Tools & Skills
    if (q.includes('learn first') || q.includes('start') || q.includes('begin') || q.includes('tools')) {
      if (career.tools?.length) {
        facts.push(`Core industry tools for ${title}: ${career.tools.slice(0, 4).join(', ')}.`);
      }
      if (career.skills?.length) {
        facts.push(`Essential foundation skills for ${title}: ${career.skills.slice(0, 4).join(', ')}.`);
      }
    }

    // 5. Salary Benchmarks
    if (q.includes('salary') || q.includes('pay') || q.includes('earn') || q.includes('compensation')) {
      if (career.salary_range_ph) {
        facts.push(`Philippine compensation benchmark for ${title}: ${career.salary_range_ph}.`);
      }
    }

    return facts;
  }
}

export const careerRetrievalService = new CareerRetrievalService();
