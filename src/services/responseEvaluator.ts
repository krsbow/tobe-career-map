/**
 * Response Quality Evaluator for Frontend
 * Evaluates generated replies against quality checks and detects canned boilerplate or bold markdown.
 */

export interface EvaluationResult {
  answers_question: boolean;
  relevant: boolean;
  uses_context_correctly: boolean;
  too_generic: boolean;
  needs_clarification: boolean;
  formatting_violation?: boolean;
  reason: string;
}

const BANNED_TEMPLATE_PHRASES = [
  'that is a thoughtful question',
  'when exploring this direction',
  'as you shape your pathway',
  'the most practical approach is to focus on hands-on fundamentals',
  'gives you the clearest picture of what the work actually feels like',
  'what specific skill, tool, or goal would you like to explore next'
];

export class ResponseEvaluator {
  evaluateResponse(userQuery: string, generatedReply: string): EvaluationResult {
    const q = userQuery.toLowerCase().trim();
    const resp = generatedReply.toLowerCase().trim();

    if (resp.length < 20) {
      return {
        answers_question: false,
        relevant: false,
        uses_context_correctly: false,
        too_generic: true,
        needs_clarification: false,
        reason: 'Response is too short or empty.',
      };
    }

    if (generatedReply.includes('**')) {
      return {
        answers_question: true,
        relevant: true,
        uses_context_correctly: true,
        too_generic: false,
        needs_clarification: false,
        formatting_violation: true,
        reason: 'Contains forbidden markdown bold syntax (**).',
      };
    }

    for (const banned of BANNED_TEMPLATE_PHRASES) {
      if (resp.includes(banned)) {
        return {
          answers_question: false,
          relevant: false,
          uses_context_correctly: false,
          too_generic: true,
          needs_clarification: false,
          reason: `Response used canned template phrase: '${banned}'.`,
        };
      }
    }

    return {
      answers_question: true,
      relevant: true,
      uses_context_correctly: true,
      too_generic: false,
      needs_clarification: false,
      reason: 'The response directly answers the user query.',
    };
  }
}

export const responseEvaluator = new ResponseEvaluator();
