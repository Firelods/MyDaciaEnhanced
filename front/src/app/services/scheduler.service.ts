import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../environment';

@Injectable({
  providedIn: 'root',
})
export class SchedulerService {
  constructor(private http: HttpClient) {}

  scheduleCharge(datetime: Date): Observable<{ message: string }> {
    return this.http.post<{ message: string }>(
      environment.baseUrl + '/plan_charge',
      {
        datetime: datetime.toISOString().replace('Z', '+00:00'),
      }
    );
  }

  scheduleAC(datetime: Date) {
    return this.http.post<{ message: string }>(
      environment.baseUrl + '/plan_ac',
      {
        datetime: datetime.toISOString().replace('Z', '+00:00'),
      }
    );
  }
}
