import { ScheduledTask } from './../../interfaces/scheduled-task';
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-scheduler',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './scheduler.component.html',
  styleUrl: './scheduler.component.scss',
})
export class SchedulerComponent {
  @Input() scheduledTask!: ScheduledTask;

  constructor() {}

  formatDate(date: Date): string {
    return `${date.getHours()}:${date.getMinutes().toLocaleString('fr-FR', {
      minimumIntegerDigits: 2,
      useGrouping: false,
    })}`;
  }

  getDay(date: Date): string {
    // if it is today, yesterday or tomorrow
    const today = new Date();
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    if (date.getDate() === today.getDate()) {
      return 'Auj.';
    } else if (date.getDate() === yesterday.getDate()) {
      return 'Hier';
    } else if (date.getDate() === tomorrow.getDate()) {
      return 'Demain';
    } else {
      return date.toDateString();
    }
  }
}
