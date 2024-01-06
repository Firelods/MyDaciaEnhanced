import { Injectable } from '@angular/core';
import { taskHistory } from '../interfaces/task-history';

@Injectable({
  providedIn: 'root',
})
export class ActionHistoryService {
  constructor() {}

  getHistory(): taskHistory[] {
    // return mock (charge or a/c on)
    return [
      {
        created_at: new Date(),
        action: 'Charge',
        success: true,
        informations: 'charge',
      },
      {
        created_at: new Date(),
        action: 'A/C',
        success: false,
        informations: 'ac',
      },
      {
        created_at: new Date(),
        action: 'Charge',
        success: false,
        informations: 'charge',
      },
      {
        created_at: new Date(),
        action: 'A/C',
        success: false,
        informations: 'ac',
      },
      {
        created_at: new Date(),
        action: 'Charge',
        success: true,
        informations: 'charge',
      },
      {
        created_at: new Date(),
        action: 'A/C',
        success: true,
        informations: 'ac',
      },
    ];
  }
}
