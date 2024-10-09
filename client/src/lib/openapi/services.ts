import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Token } from './models';

export type AuthData = {};

export class AuthService {
	/**
	 * Login
	 * Generate login url and redirect
	 * @throws ApiError
	 */
	public static authLogin(): CancelablePromise<void> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/auth/login',
			errors: {
				307: `Successful Response`
			}
		});
	}

	/**
	 * Callback
	 * Process login response from Google and return user info
	 * @throws ApiError
	 */
	public static authCallback(): CancelablePromise<void> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/auth/callback',
			errors: {
				307: `Successful Response`
			}
		});
	}

	/**
	 * Token
	 * Get infomation(and token) of user
	 * @returns Token Successful Response
	 * @throws ApiError
	 */
	public static authToken(): CancelablePromise<Token> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/auth/token'
		});
	}

	/**
	 * Logout
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static authLogout(): CancelablePromise<unknown> {
		return __request(OpenAPI, {
			method: 'POST',
			url: '/auth/logout'
		});
	}
}
