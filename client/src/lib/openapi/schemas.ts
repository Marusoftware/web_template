export const $Token = {
	properties: {
		id: {
			type: 'string',
			isRequired: true
		},
		name: {
			type: 'string',
			isRequired: true
		},
		email: {
			type: 'string',
			isRequired: true,
			format: 'email'
		},
		token: {
			type: 'string',
			isRequired: true
		}
	}
} as const;
