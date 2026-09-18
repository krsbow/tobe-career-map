import { ReactNode, useEffect, useState } from 'react';
import Nav from './Nav';

export default function AppShell({ children }: { children: ReactNode }) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 20);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--background)' }}>
      <Nav />
      <main
        style={{
          flex: 1,
          paddingTop: 60,
          opacity: visible ? 1 : 0,
          transition: 'opacity 0.3s ease',
        }}
      >
        {children}
      </main>
      <footer
        style={{
          borderTop: '1px solid var(--border)',
          padding: '24px 32px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: 12,
          background: 'rgba(249,248,245,0.6)',
          zIndex: 10,
        }}
      >
        <span style={{ fontFamily: 'var(--font-display)', fontSize: 16, fontWeight: 500, color: 'var(--navy)', letterSpacing: '-0.02em' }}>
          TO BE
        </span>
        <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: 0 }}>
          &copy; 2026 TO BE. Career discovery for the curious.
        </p>
        <p style={{ fontSize: 13, color: 'var(--muted-foreground)', margin: 0 }}>
          created by krsbow
        </p>
      </footer>
    </div>
  );
}
