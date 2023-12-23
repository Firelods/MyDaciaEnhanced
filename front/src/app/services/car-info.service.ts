import { Injectable } from '@angular/core';
import { CarInfo } from '../interfaces/car-info';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environment';

@Injectable({
  providedIn: 'root',
})
export class CarInfoService {
  constructor(private http: HttpClient) {}

  getCarInfo(): Observable<CarInfo> {
    return this.http.get<CarInfo>(environment.baseUrl + '/car_info');
  }
}
