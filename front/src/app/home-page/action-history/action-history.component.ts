import { Component, Input } from '@angular/core';

import { taskHistory } from '../../interfaces/task-history';

@Component({
  selector: 'app-action-history',
  standalone: true,
  imports: [],
  templateUrl: './action-history.component.html',
  styleUrl: './action-history.component.scss',
})
export class ActionHistoryComponent {
  @Input() history: taskHistory[] = [];
  constructor() {
    console.log(this.history);
  }
  formatHour(date: Date): string {
    return `${date.getHours()}:${date
      .getMinutes()
      .toLocaleString('fr-FR', {
        minimumIntegerDigits: 2,
        useGrouping: false,
      })}`;
  }
  formatDate(date: Date): string {
    return `${date.getDate()}/${date.getMonth() + 1}`;
  }
}
