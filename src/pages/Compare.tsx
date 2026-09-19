import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import AppShell from '../components/AppShell';
import TOBEWidget from '../components/TOBEWidget';
import { useCareer } from '../context/CareerContext';
import { Career } from '../data/careersData';

export default function Compare() {
  const navigate = useNavigate();
  const { careers, getCareerMatchDetails, assessmentResults, createOrSetRoadmap, recordView } = useCareer();

  const [selectedCareers, setSelectedCareers] = useState<Career[]>([
    careers.find((c) => c.id === 'frontend-developer') || careers[0],
    careers.find((c) => c.id === 'ux-designer') || careers[1],
  ]);
  const [pickerSlot, setPickerSlot] = useState<number | null>(null);

  const handleSelectCareer = (slot: number, career: Career) => {
    const updated = [...selectedCareers];
    updated[slot] = career;
    setSelectedCareers(updated);
    setPickerSlot(null);
  };

  const addSlot = () => {
    if (selectedCareers.length < 3) {
      const remaining = careers.find((c) => !selectedCareers.some((s) => s.id === c.id));
      if (remaining) setSelectedCareers([...selectedCareers, remaining]);
    }
  };

  const removeSlot = (slotIdx: number) => {
    if (selectedCareers.length > 2) {
      setSelectedCareers(selectedCareers.filter((_, idx) => idx !== slotIdx));
    }
  };

  const comparisonAttributes = [
    {
      id: 'category',
      label: 'Domain Category',
      render: (c: Career) => (
        <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--navy)' }}>
          {c.category_name}
        </span>
      ),
    },
    {
      id: 'work_style',
      label: 'Work Style & Dynamic',
      render: (c: Career) => (
        <div style={{ fontSize: 13, color: 'var(--foreground)', fontWeight: 500 }}>
          {c.work_style}
        </div>
      ),
    },
    {
      id: 'education',
      label: 'Typical Preparation',
      render: (c: Career) => (
        <div style={{ fontSize: 13, color: 'var(--foreground)' }}>
          {c.education_paths[0] || 'Degree or Technical Certification'}
        </div>
      ),
    },
    {
      id: 'alignment',
      label: 'Assessment Alignment',
      render: (c: Career) => {
        if (!assessmentResults) {
          return <span style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>Take assessment to view tier</span>;
        }
        const match = getCareerMatchDetails(c);
        const isStrong = match.tier === 'Strong alignment';
        const isWorth = match.tier === 'Worth exploring';
        return (
          <div>
            <span
              style={{
                fontSize: 12,
                fontWeight: 700,
                padding: '3px 8px',
                borderRadius: 10,
                background: isStrong ? '#ECFDF5' : isWorth ? '#EFF6FF' : '#F8FAFC',
                color: isStrong ? '#065F46' : isWorth ? '#1E40AF' : '#475569',
                border: `1px solid ${isStrong ? '#A7F3D0' : isWorth ? '#BFDBFE' : '#E2E8F0'}`,
                display: 'inline-block',
                marginBottom: 4,
              }}
            >
              ● {match.tier}
            </span>
            <div style={{ fontSize: 11, color: 'var(--muted-foreground)' }}>
              Matched to interest profile
            </div>
          </div>
        );
      },
    },
    {
      id: 'ph_salary',
      label: 'Philippines Salary (PHP)',
      render: (c: Career) => (
        <div>
          <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--foreground)' }}>
            {c.salary_data.philippines.entry_level}
          </div>
          <div style={{ fontSize: 11, color: 'var(--muted-foreground)', marginTop: 2 }}>
            Mid: {c.salary_data.philippines.mid_level.split('(')[0]}
          </div>
        </div>
      ),
    },
    {
      id: 'global_salary',
      label: 'Global Remote (USD)',
      render: (c: Career) => (
        <div>
          <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--foreground)' }}>
            {c.salary_data.global_usd.entry_level}
          </div>
          <div style={{ fontSize: 11, color: 'var(--muted-foreground)', marginTop: 2 }}>
            Senior: {c.salary_data.global_usd.senior_level}
          </div>
        </div>
      ),
    },
    {
      id: 'work_style',
      label: 'Working Style & Rhythm',
      render: (c: Career) => (
        <span style={{ fontSize: 13, color: 'var(--foreground)', lineHeight: 1.5 }}>
          {c.work_style}
        </span>
      ),
    },
    {
      id: 'core_skills',
      label: 'Core Skills Required',
      render: (c: Career) => (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 4 }}>
          {c.core_skills.map((s) => (
            <span key={s} style={{ fontSize: 11, padding: '2px 6px', background: 'var(--secondary)', color: 'var(--navy)', borderRadius: 4 }}>
              {s}
            </span>
          ))}
        </div>
      ),
    },
    {
      id: 'education_paths',
      label: 'Primary Education & Licensure',
      render: (c: Career) => (
        <ul style={{ margin: 0, paddingLeft: 16, fontSize: 12, color: 'var(--foreground)', lineHeight: 1.5 }}>
          {c.education_paths.map((p, idx) => (
            <li key={idx} style={{ marginBottom: 3 }}>{p}</li>
          ))}
        </ul>
      ),
    },
    {
      id: 'credentials',
      label: 'Key Credentials & Certs',
      render: (c: Career) => (
        <div style={{ fontSize: 12 }}>
          {c.certifications.slice(0, 2).map((cert, idx) => (
            <div key={idx} style={{ marginBottom: 4 }}>
              <span style={{ fontWeight: 600, color: 'var(--navy)' }}>{cert.name}</span>
              <span style={{ fontSize: 11, color: 'var(--muted-foreground)', display: 'block' }}>Provider: {cert.provider} ({cert.cost})</span>
            </div>
          ))}
        </div>
      ),
    },
  ];

  return (
    <AppShell>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '56px 32px 80px' }}>
        <div style={{ marginBottom: 40 }}>
          <p style={{ fontSize: 12, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 6 }}>
            Multi-Domain Comparison Matrix
          </p>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 4.5vw, 42px)', fontWeight: 400, letterSpacing: '-0.025em', color: 'var(--foreground)', margin: '0 0 12px' }}>
            Compare pathways side by side.
          </h1>
          <p style={{ fontSize: 15, color: 'var(--muted-foreground)', maxWidth: 680, lineHeight: 1.6 }}>
            Analyze tradeoffs in salary, daily rhythms, licensure prerequisites, and skill requirements across multiple career options without artificial winners.
          </p>
        </div>

        {/* Matrix comparison grid */}
        <div style={{ background: 'var(--card)', border: '1px solid var(--border)', borderRadius: 'calc(var(--radius) * 2)', overflowX: 'auto', boxShadow: '0 4px 16px rgba(0,0,0,0.03)' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', minWidth: 720 }}>
            <thead>
              <tr style={{ borderBottom: '2px solid var(--border)', background: '#FAF9F6' }}>
                <th style={{ padding: '24px 20px', width: '22%', fontSize: 13, fontWeight: 700, color: 'var(--muted-foreground)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                  Attribute
                </th>
                {selectedCareers.map((c, slotIdx) => (
                  <th key={slotIdx} style={{ padding: '20px', width: `${78 / selectedCareers.length}%`, verticalAlign: 'top', position: 'relative' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 8 }}>
                      <button
                        onClick={() => setPickerSlot(slotIdx)}
                        style={{
                          background: 'none',
                          border: 'none',
                          fontSize: 12,
                          fontWeight: 600,
                          color: 'var(--navy)',
                          cursor: 'pointer',
                          textDecoration: 'underline',
                          padding: 0,
                        }}
                      >
                        Change Role ▾
                      </button>
                      {selectedCareers.length > 2 && (
                        <button
                          onClick={() => removeSlot(slotIdx)}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: 'var(--muted-foreground)',
                            cursor: 'pointer',
                            fontSize: 14,
                            padding: 0,
                          }}
                          title="Remove column"
                        >
                          ✕
                        </button>
                      )}
                    </div>
                    <div
                      style={{
                        fontFamily: 'var(--font-display)',
                        fontSize: 20,
                        fontWeight: 500,
                        color: 'var(--foreground)',
                        marginBottom: 4,
                        cursor: 'pointer',
                      }}
                      onClick={() => {
                        recordView(c.id);
                        navigate(`/career/${c.id}`);
                      }}
                    >
                      {c.title}
                    </div>
                    <p style={{ fontSize: 12, color: 'var(--muted-foreground)', margin: '0 0 8px', lineHeight: 1.4, fontWeight: 400 }}>
                      {c.tagline}
                    </p>
                    <button
                      onClick={() => {
                        recordView(c.id);
                        navigate(`/career/${c.id}`);
                      }}
                      style={{
                        background: 'none',
                        border: 'none',
                        fontSize: 12,
                        fontWeight: 600,
                        color: 'var(--navy)',
                        cursor: 'pointer',
                        padding: 0,
                      }}
                    >
                      Explore Details →
                    </button>
                  </th>
                ))}
                {selectedCareers.length < 3 && (
                  <th style={{ padding: '20px', width: '15%', verticalAlign: 'middle', textAlign: 'center' }}>
                    <button
                      onClick={addSlot}
                      style={{
                        background: 'transparent',
                        border: '1.5px dashed var(--border)',
                        borderRadius: 'var(--radius)',
                        padding: '12px 16px',
                        fontSize: 13,
                        fontWeight: 600,
                        color: 'var(--navy)',
                        cursor: 'pointer',
                      }}
                    >
                      + Add Career
                    </button>
                  </th>
                )}
              </tr>
            </thead>
            <tbody>
              {comparisonAttributes.map((attr, idx) => (
                <tr key={attr.id} style={{ borderBottom: '1px solid var(--border)', background: idx % 2 === 0 ? 'white' : '#FCFCF9' }}>
                  <td style={{ padding: '16px 20px', fontSize: 13, fontWeight: 700, color: 'var(--navy)', verticalAlign: 'top' }}>
                    {attr.label}
                  </td>
                  {selectedCareers.map((c, slotIdx) => (
                    <td key={slotIdx} style={{ padding: '16px 20px', verticalAlign: 'top' }}>
                      {attr.render(c)}
                    </td>
                  ))}
                  {selectedCareers.length < 3 && <td />}
                </tr>
              ))}
              <tr>
                <td style={{ padding: '20px', fontSize: 13, fontWeight: 700, color: 'var(--navy)' }}>
                  Action
                </td>
                {selectedCareers.map((c, slotIdx) => (
                  <td key={slotIdx} style={{ padding: '20px' }}>
                    <button
                      onClick={() => {
                        createOrSetRoadmap(c.id);
                        navigate('/my-path');
                      }}
                      style={{
                        background: 'var(--primary)',
                        color: 'white',
                        border: 'none',
                        borderRadius: 'var(--radius)',
                        padding: '10px 18px',
                        fontSize: 13,
                        fontWeight: 600,
                        cursor: 'pointer',
                        width: '100%',
                      }}
                    >
                      Start My Path →
                    </button>
                  </td>
                ))}
                {selectedCareers.length < 3 && <td />}
              </tr>
            </tbody>
          </table>
        </div>

        {/* Career Picker Modal */}
        {pickerSlot !== null && (
          <div
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              background: 'rgba(26,31,46,0.5)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              zIndex: 9999,
              padding: 20,
            }}
            onClick={() => setPickerSlot(null)}
          >
            <div
              style={{
                background: 'var(--background)',
                borderRadius: 'calc(var(--radius) * 1.5)',
                maxWidth: 600,
                width: '100%',
                maxHeight: '75vh',
                overflowY: 'auto',
                padding: '28px',
                border: '1px solid var(--border)',
              }}
              onClick={(e) => e.stopPropagation()}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: 22, margin: 0 }}>
                  Select Career to Compare
                </h3>
                <button
                  onClick={() => setPickerSlot(null)}
                  style={{ background: 'none', border: 'none', fontSize: 20, cursor: 'pointer', color: 'var(--muted-foreground)' }}
                >
                  ✕
                </button>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                {careers.map((career) => (
                  <button
                    key={career.id}
                    onClick={() => handleSelectCareer(pickerSlot, career)}
                    style={{
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      padding: '12px 16px',
                      textAlign: 'left',
                      cursor: 'pointer',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    }}
                  >
                    <div>
                      <div style={{ fontWeight: 600, fontSize: 14, color: 'var(--foreground)' }}>{career.title}</div>
                      <div style={{ fontSize: 12, color: 'var(--muted-foreground)' }}>{career.category_name}</div>
                    </div>
                    <span style={{ fontSize: 12, color: 'var(--navy)', fontWeight: 600 }}>Select →</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
      <TOBEWidget />
    </AppShell>
  );
}
