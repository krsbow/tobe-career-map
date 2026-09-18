import { useState } from 'react';
import AppShell from '../components/AppShell';

type CareerOption = {
  title: string;
  field: string;
  salary: string;
  salaryMid: number;
  growth: string;
  match: number;
  workStyle: string;
  education: string;
  stress: string;
  creativity: string;
  social: string;
  advancement: string;
};

const careerOptions: CareerOption[] = [
  { title: 'UX Designer', field: 'Design', salary: '$95k – $145k', salaryMid: 120, growth: '+18%', match: 94, workStyle: 'Remote-friendly', education: "Bachelor's or self-taught", stress: 'Moderate', creativity: 'Very high', social: 'Moderate', advancement: 'Strong' },
  { title: 'Product Manager', field: 'Product', salary: '$110k – $175k', salaryMid: 142, growth: '+21%', match: 89, workStyle: 'Hybrid', education: "Bachelor's + experience", stress: 'High', creativity: 'High', social: 'Very high', advancement: 'Very strong' },
  { title: 'UX Researcher', field: 'Research', salary: '$88k – $130k', salaryMid: 109, growth: '+16%', match: 85, workStyle: 'Often remote', education: "Bachelor's in Psychology", stress: 'Low-Moderate', creativity: 'High', social: 'High', advancement: 'Moderate' },
  { title: 'Data Analyst', field: 'Analytics', salary: '$72k – $115k', salaryMid: 93, growth: '+23%', match: 79, workStyle: 'Remote-friendly', education: "Bachelor's in Math/CS", stress: 'Moderate', creativity: 'Moderate', social: 'Low', advancement: 'Strong' },
  { title: 'Brand Strategist', field: 'Marketing', salary: '$75k – $120k', salaryMid: 97, growth: '+14%', match: 76, workStyle: 'Hybrid', education: "Bachelor's in Marketing", stress: 'Moderate', creativity: 'Very high', social: 'High', advancement: 'Moderate' },
  { title: 'Therapist', field: 'Healthcare', salary: '$60k – $98k', salaryMid: 79, growth: '+15%', match: 68, workStyle: 'Telehealth options', education: "Master's required", stress: 'High', creativity: 'Moderate', social: 'Very high', advancement: 'Steady' },
];

const metrics = [
  { key: 'salary', label: 'Salary range' },
  { key: 'growth', label: 'Job growth' },
  { key: 'match', label: 'Your match' },
  { key: 'workStyle', label: 'Work style' },
  { key: 'education', label: 'Education needed' },
  { key: 'stress', label: 'Stress level' },
  { key: 'creativity', label: 'Creative demand' },
  { key: 'social', label: 'Social interaction' },
  { key: 'advancement', label: 'Advancement' },
] as const;

function getMatchColor(match: number) {
  if (match >= 90) return 'var(--sage)';
  if (match >= 80) return 'var(--navy-light)';
  return 'var(--muted-foreground)';
}

export default function Compare() {
  const [selected, setSelected] = useState<CareerOption[]>([careerOptions[0], careerOptions[1]]);
  const [pickerOpen, setPickerOpen] = useState<number | null>(null);

  const toggleCareer = (slot: number, career: CareerOption) => {
    const newSelected = [...selected];
    newSelected[slot] = career;
    setSelected(newSelected);
    setPickerOpen(null);
  };

  const addSlot = () => {
    if (selected.length < 3) {
      const remaining = careerOptions.find((c) => !selected.find((s) => s.title === c.title));
      if (remaining) setSelected([...selected, remaining]);
    }
  };

  const removeSlot = (i: number) => {
    setSelected(selected.filter((_, idx) => idx !== i));
  };

  const renderValue = (career: CareerOption, key: typeof metrics[number]['key']) => {
    if (key === 'match') {
      return (
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <div style={{ flex: 1, height: 4, background: 'var(--border)', borderRadius: 2, overflow: 'hidden' }}>
            <div
              style={{
                height: '100%',
                width: `${career.match}%`,
                background: getMatchColor(career.match),
                borderRadius: 2,
                transition: 'width 0.8s ease',
              }}
            />
          </div>
          <span style={{ fontSize: 13, fontWeight: 700, color: getMatchColor(career.match), whiteSpace: 'nowrap' }}>
            {career.match}%
          </span>
        </div>
      );
    }
    if (key === 'salary') return <span style={{ fontSize: 14, fontWeight: 600 }}>{career.salary}</span>;
    if (key === 'growth') return (
      <span style={{ color: 'var(--sage)', fontWeight: 700, fontSize: 14 }}>{career.growth}</span>
    );
    return <span style={{ fontSize: 14, color: 'var(--foreground)' }}>{career[key]}</span>;
  };

  return (
    <AppShell>
      <div style={{ maxWidth: 1100, margin: '0 auto', padding: '56px 32px 80px' }}>
        <div style={{ marginBottom: 48 }}>
          <p style={{ fontSize: 13, fontWeight: 600, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--muted-foreground)', marginBottom: 8 }}>
            Compare
          </p>
          <h1 style={{ fontFamily: 'var(--font-display)', fontSize: 'clamp(28px, 5vw, 44px)', fontWeight: 400, letterSpacing: '-0.025em', color: 'var(--foreground)' }}>
            See careers side by side.
          </h1>
        </div>

        {/* Career selectors */}
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: `repeat(${selected.length}, 1fr) ${selected.length < 3 ? '60px' : ''}`,
            gap: 12,
            marginBottom: 2,
          }}
        >
          {selected.map((career, i) => (
            <div key={i} style={{ position: 'relative' }}>
              <div
                style={{
                  background: 'var(--primary)',
                  borderRadius: 'calc(var(--radius) * 2) calc(var(--radius) * 2) 0 0',
                  padding: '20px 20px 16px',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div style={{ fontSize: 11, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.45)', marginBottom: 4 }}>
                      {career.field}
                    </div>
                    <button
                      onClick={() => setPickerOpen(pickerOpen === i ? null : i)}
                      style={{
                        background: 'none',
                        border: 'none',
                        fontFamily: 'var(--font-display)',
                        fontSize: 20,
                        fontWeight: 400,
                        color: 'white',
                        cursor: 'pointer',
                        padding: 0,
                        textAlign: 'left',
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                        letterSpacing: '-0.02em',
                      }}
                    >
                      {career.title}
                      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="rgba(255,255,255,0.5)" strokeWidth="1.5">
                        <path d="M3 5l4 4 4-4" strokeLinecap="round" strokeLinejoin="round" />
                      </svg>
                    </button>
                  </div>
                  {selected.length > 2 && (
                    <button
                      onClick={() => removeSlot(i)}
                      style={{ background: 'none', border: 'none', color: 'rgba(255,255,255,0.4)', cursor: 'pointer', padding: 0 }}
                    >
                      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="1.5">
                        <line x1="3" y1="3" x2="11" y2="11" /><line x1="11" y1="3" x2="3" y2="11" />
                      </svg>
                    </button>
                  )}
                </div>

                {/* Picker dropdown */}
                {pickerOpen === i && (
                  <div
                    style={{
                      position: 'absolute',
                      top: '100%',
                      left: 0,
                      right: 0,
                      zIndex: 50,
                      background: 'var(--card)',
                      border: '1px solid var(--border)',
                      borderRadius: 'var(--radius)',
                      boxShadow: '0 8px 32px rgba(26,31,46,0.12)',
                      overflow: 'hidden',
                    }}
                  >
                    {careerOptions
                      .filter((c) => !selected.find((s, si) => s.title === c.title && si !== i))
                      .map((c) => (
                        <button
                          key={c.title}
                          onClick={() => toggleCareer(i, c)}
                          style={{
                            width: '100%',
                            padding: '12px 16px',
                            border: 'none',
                            background: 'none',
                            textAlign: 'left',
                            fontSize: 14,
                            fontFamily: 'var(--font-body)',
                            fontWeight: 500,
                            color: 'var(--foreground)',
                            cursor: 'pointer',
                            borderBottom: '1px solid var(--border)',
                            transition: 'background 0.15s ease',
                          }}
                          onMouseEnter={(e) => { (e.target as HTMLElement).style.background = 'var(--muted)'; }}
                          onMouseLeave={(e) => { (e.target as HTMLElement).style.background = 'none'; }}
                        >
                          {c.title}
                          <span style={{ fontSize: 12, color: 'var(--muted-foreground)', marginLeft: 8 }}>{c.field}</span>
                        </button>
                      ))}
                  </div>
                )}
              </div>
            </div>
          ))}

          {selected.length < 3 && (
            <button
              onClick={addSlot}
              style={{
                background: 'var(--muted)',
                border: '1px dashed var(--border)',
                borderRadius: 'calc(var(--radius) * 2) calc(var(--radius) * 2) 0 0',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--muted-foreground)',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => { (e.currentTarget).style.background = 'var(--secondary)'; }}
              onMouseLeave={(e) => { (e.currentTarget).style.background = 'var(--muted)'; }}
            >
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5">
                <line x1="10" y1="4" x2="10" y2="16" strokeLinecap="round" />
                <line x1="4" y1="10" x2="16" y2="10" strokeLinecap="round" />
              </svg>
            </button>
          )}
        </div>

        {/* Metrics table */}
        <div
          style={{
            border: '1px solid var(--border)',
            borderTop: 'none',
            borderRadius: `0 0 calc(var(--radius) * 2) calc(var(--radius) * 2)`,
            overflow: 'hidden',
          }}
        >
          {metrics.map((metric, mi) => (
            <div
              key={metric.key}
              style={{
                display: 'grid',
                gridTemplateColumns: `180px repeat(${selected.length}, 1fr)`,
                borderBottom: mi < metrics.length - 1 ? '1px solid var(--border)' : 'none',
                background: mi % 2 === 0 ? 'var(--card)' : 'var(--background)',
              }}
            >
              <div
                style={{
                  padding: '16px 20px',
                  fontSize: 13,
                  fontWeight: 600,
                  color: 'var(--muted-foreground)',
                  borderRight: '1px solid var(--border)',
                  display: 'flex',
                  alignItems: 'center',
                }}
              >
                {metric.label}
              </div>
              {selected.map((career, ci) => (
                <div
                  key={ci}
                  style={{
                    padding: '16px 20px',
                    borderRight: ci < selected.length - 1 ? '1px solid var(--border)' : 'none',
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  {renderValue(career, metric.key)}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>

      <style>{`
        @media (max-width: 768px) {
          div[style*="grid-template-columns: 180px"] {
            grid-template-columns: 120px repeat(2, 1fr) !important;
          }
        }
      `}</style>
    </AppShell>
  );
}
