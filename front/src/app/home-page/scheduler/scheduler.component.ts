import { ScheduledTask } from './../../interfaces/scheduled-task';
import {
  AfterViewInit,
  Component,
  ElementRef,
  Input,
  ViewChild,
} from '@angular/core';

import { SchedulerService } from '../../services/scheduler.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-scheduler',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './scheduler.component.html',
  styleUrl: './scheduler.component.scss',
})
export class SchedulerComponent implements AfterViewInit {
  @Input() scheduledTask!: ScheduledTask;
  @Input() type!: string;
  @ViewChild('inputScheduleDate') inputScheduleDate!: ElementRef;
  @ViewChild('inputScheduleTime') inputScheduleTime!: ElementRef;

  constructor(private scheduler: SchedulerService) {}

  ngAfterViewInit(): void {
    this.inputScheduleDate.nativeElement.min = new Date()
      .toISOString()
      .split('T')[0];
    this.inputScheduleDate.nativeElement.click();
  }

  formatDate(date: Date): string {
    return `${date.getHours()}:${date.getMinutes().toLocaleString('fr-FR', {
      minimumIntegerDigits: 2,
      useGrouping: false,
    })}`;
  }

  onDateChange($event: Event) {
    setTimeout(() => {
      this.inputScheduleTime.nativeElement.click();
    }, 200);
  }
  onTimeChange($event: Event) {
    this.scheduleTask();
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

  activateInput(): void {
    this.inputScheduleDate.nativeElement.click();
  }

  scheduleTask(): void {
    console.log(this.scheduledTask);

    if (this.type == 'charge') {
      // build datetime from date and time inputs
      let datetime = new Date(
        this.inputScheduleDate.nativeElement.value +
          'T' +
          this.inputScheduleTime.nativeElement.value
      );
      this.scheduler.scheduleCharge(datetime).subscribe((res) => {
        // TODO: make notification
        this.scheduledTask!.timestamp = datetime;
      });
    } else if (this.scheduledTask.type == 'ac') {
      this.scheduler.scheduleAC(
        new Date(this.inputScheduleTime.nativeElement.value)
      );
    }
  }
}
