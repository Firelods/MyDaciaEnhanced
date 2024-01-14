import { Injectable } from '@angular/core';
import { CarInfo } from '../interfaces/car-info';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environment';
import { MOCK_CAR_INFO } from './mock/car-info';

@Injectable({
  providedIn: 'root',
})
export class CarInfoService {
  constructor(private http: HttpClient) {}

  getCarInfo(): Observable<CarInfo> {
    if (environment.mock) {
      return of(MOCK_CAR_INFO);
    }
    return this.http.get<CarInfo>(environment.baseUrl + '/car_info');
  }
}
