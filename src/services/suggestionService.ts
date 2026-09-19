/**
 * Decoupled Downstream Suggestion Service for Frontend
 * Generates follow-up question chips strictly after response generation.
 */

export class SuggestionService {
  generateFollowUps(userQuery: string, responseText: string): string[] {
    const q = userQuery.toLowerCase();

    if (q.includes('design') || q.includes('draw') || q.includes('drawing') || q.includes('figma') || q.includes('ui') || q.includes('ux')) {
      return [
        'What tools do UI/UX designers actually use daily?',
        'What is the difference between UI and UX?',
        'What should I learn first in Figma?',
      ];
    }

    if (q.includes('smart') || q.includes('scared') || q.includes('afraid') || q.includes('good enough') || q.includes('doubt')) {
      return [
        'How many hours a day should I practice?',
        'What should I learn first?',
        'What if I get completely stuck on a problem?',
      ];
    }

    if (q.includes('two hours') || q.includes('2 hours') || q.includes('schedule') || q.includes('busy') || q.includes('school')) {
      return [
        'What beginner projects fit a 2-hour daily schedule?',
        'What should I learn first?',
        'How do I track my learning milestones?',
      ];
    }

    if (q.includes('unsure') || q.includes('not sure') || q.includes('dont know') || q.includes("don't know") || q.includes('like this')) {
      return [
        'What are other careers that might fit me?',
        'How can I test a career in one weekend?',
        'Can I combine creative and technical work?',
      ];
    }

    if (q.includes('learn first') || q.includes('start') || q.includes('begin') || q.includes('first step')) {
      return [
        'How long does it usually take to become job-ready?',
        'What kind of projects should I build first?',
        'Do I need a degree to get hired?',
      ];
    }

    if (q.includes('degree') || q.includes('college') || q.includes('university') || q.includes('prc')) {
      return [
        'What kind of projects should I put in my portfolio?',
        'What certifications carry weight with employers?',
        'How do I land an entry-level role without experience?',
      ];
    }

    return [
      'What should I learn first?',
      'What does a normal workday look like?',
      'How much time should I invest each week?',
    ];
  }
}

export const suggestionService = new SuggestionService();
