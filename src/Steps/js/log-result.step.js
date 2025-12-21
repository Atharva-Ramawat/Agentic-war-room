export const config = {
  name: 'LogAnalyzeResult',
  type: 'event',
  subscribes: ['analyze-result'],
  emits: [],                  // ✅ REQUIRED
  flows: ['ai-war-room-flow']
};

export const handler = async (input, { logger }) => {
  logger.info('AI War Room analysis complete', input);
};
