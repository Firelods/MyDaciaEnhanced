import { Injectable } from '@angular/core';
import { CarInfo } from '../interfaces/car-info';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environment';

@Injectable({
  providedIn: 'root',
})
export class CarInfoService {
  constructor(private http: HttpClient) {}

  getCarInfo(): Observable<CarInfo> {
    // return this.http.get<CarInfo>(environment.baseUrl + '/car_info');
    return of({
      autonomy: 207,
      batteryLevel: 97,
      charging: false,
      climate: false,
      history: [
        {
          action: 'charge',
          created_at: new Date('2024-01-06T17:10:59.000Z'),
          informations: '',
          login_id: 'contact@clement-lefevre.fr',
          success: true,
        },
        {
          action: 'charge',
          created_at: new Date('2024-01-06T17:22:01.000Z'),
          informations: '',
          login_id: 'contact@clement-lefevre.fr',
          success: true,
        },
        {
          action: 'charge',
          created_at: new Date('2024-01-06T18:10:02.000Z'),
          informations: '',
          login_id: 'contact@clement-lefevre.fr',
          success: true,
        },
      ],
      imageUrl:
        'https://static.renault.co.uk/cms/version/2021-01/renault-logo-2020.png',
      lastRefresh: new Date('2024-01-06T14:13:07Z'),
      name: 'SPRING',
      scheduled: {
        airConditioning: { type: 'ac' },
        charging: { type: 'charge' },
      },
      totalKilometers: 3366.88,
    });
  }
}
