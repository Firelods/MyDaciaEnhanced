import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { environment } from '../environment';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient, private router: Router) {}

  login(email: string, password: string) {
    this.http
      .post<{ message: string; token: string }>(
        environment.baseUrl + '/login',
        { email, password }
      )
      .subscribe((response) => {
        const token = response.token;
        console.log(response);

        if (token) {
          localStorage.setItem('token', token);
          this.router.navigate(['/']);
        }
      });
  }

  init_renault_login(email: string, password: string) {
    this.http
      .post<{ message: string; token: string }>(
        environment.baseUrl + '/init_renault_session',
        { email, password }
      )
      .subscribe((response) => {
        const token = response.token;
        console.log(response);

        if (token) {
          localStorage.setItem('token', token);
          this.router.navigate(['/']);
        }
      });
  }
}
