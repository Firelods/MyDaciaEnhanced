import { Injectable } from '@angular/core';
import { taskHistory } from '../interfaces/task-history';

@Injectable({
  providedIn: 'root'
})
export class ActionHistoryService {

  constructor() { }

  getHistory(): taskHistory[] {
    // return mock (charge or a/c on)
    return [
      {
        timestamp: new Date(),
        task: 'Charge',
        success: true,
        type: 'charge'
      },
      {
        timestamp: new Date(),
        task: 'A/C',
        success: false,
        type: 'ac'
      },
      {
        timestamp: new Date(),
        task: 'Charge',
        success: false,
        type: 'charge'
      },
      {
        timestamp: new Date(),
        task: 'A/C',
        success: false,
        type: 'ac'
      },
      {
        timestamp: new Date(),
        task: 'Charge',
        success: true,
        type: 'charge'
      },
      {
        timestamp: new Date(),
        task: 'A/C',
        success: true,
        type: 'ac'
      },

    ]

  }
}
