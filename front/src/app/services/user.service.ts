import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { environment } from '../environment';
import { Router } from '@angular/router';
import { VehicleList } from '../interfaces/vehicle-list';
import { Observable, of } from 'rxjs';

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

  init_renault_login(
    email: string,
    password: string
  ): Observable<VehicleList[]> {
    if (environment.mock) {
      return of([
        {
          model: 'Spring',
          vin: 'VF1RFA00V6V000000',
          licensePlate: 'AA-000-AA',
        },
      ]);
    }
    return this.http.post<VehicleList[]>(
      environment.baseUrl + '/init_renault_session',
      {
        email,
        password,
      }
    );
  }

  chooseVehicle(vin: string) {
    this.http
      .post(environment.baseUrl + '/set_vin', {
        vin,
      })
      .subscribe((response) => {
        console.log(response);
        this.router.navigate(['/']);
      });
  }
}
