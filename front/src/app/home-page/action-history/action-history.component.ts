import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { taskHistory } from '../../interfaces/task-history';

@Component({
  selector: 'app-action-history',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './action-history.component.html',
  styleUrl: './action-history.component.scss'
})
export class ActionHistoryComponent {
  @Input() history: taskHistory[] = [];

  formatHour(date: Date): string {
    return `${date.getHours()}:${date.getMinutes().toLocaleString('fr-FR', { minimumIntegerDigits: 2, useGrouping: false })}`;
  }
  formatDate(date: Date): string {
    return `${date.getDate()}/${date.getMonth() + 1}`;
  }
}
