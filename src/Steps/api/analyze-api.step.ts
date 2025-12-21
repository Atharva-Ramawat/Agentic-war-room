import type { ApiRouteConfig, Handlers } from 'motia';

export const config: ApiRouteConfig = {
  name: 'AnalyzeAPI',
  type: 'api',
  path: '/analyze',
  method: 'POST',

  emits: ['analyze-request'],
  flows: ['ai-war-room-flow'],

  responseSchema: {
    200: {
      type: 'object',
      properties: {
        status: { type: 'string' },
        requestId: { type: 'string' }
      }
    }
  }
};

export const handler: Handlers['AnalyzeAPI'] = async (req, { emit }) => {
  const requestId = crypto.randomUUID();

  await emit({
    topic: 'analyze-request',
    data: {
      requestId,
      text: req.body?.text
    }
  });

  return {
    status: 200,
    body: {
      status: 'processing',
      requestId
    }
  };
};
    