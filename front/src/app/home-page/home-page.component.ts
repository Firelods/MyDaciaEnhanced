import { ActionHistoryService } from './../services/action-history.service';
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';
import { FooterComponent } from '../footer/footer.component';
import { CarInfoService } from '../services/car-info.service';
import { CarInfo } from '../interfaces/car-info';
import { SchedulerComponent } from './scheduler/scheduler.component';
import { ActionHistoryComponent } from './action-history/action-history.component';
import { taskHistory } from '../interfaces/task-history';
@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    CommonModule,
    FooterComponent,
    SchedulerComponent,
    ActionHistoryComponent,
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss',
})
export class HomePageComponent {
  actualCar!: CarInfo;
  history: taskHistory[] = [];
  percentage = 65;
  @ViewChild('circlePath')
  circlePath!: ElementRef;

  constructor(
    private carInfoService: CarInfoService,
    private datePipe: DatePipe,
    private ActionHistoryService: ActionHistoryService
  ) {
    this.carInfoService.getCarInfo().subscribe((carInfo) => {
      this.actualCar = carInfo;
      this.drawGauge();
      this.actualCar.history.forEach((history) => {
        history.created_at = new Date(history.created_at);
      });
      if (this.actualCar.scheduled.airConditioning.timestamp) {
        this.actualCar.scheduled.airConditioning!.timestamp = new Date(
          this.actualCar.scheduled.airConditioning.timestamp
        );
      }
      if (this.actualCar.scheduled.charging.timestamp) {
        this.actualCar.scheduled.charging.timestamp = new Date(
          this.actualCar.scheduled.charging.timestamp
        );
      }
      console.log(this.actualCar);
    });
    this.history = this.ActionHistoryService.getHistory();
  }

  formatDate(date: Date): string {
    let hours = this.datePipe.transform(date, 'HH');
    let minutes = this.datePipe.transform(date, 'mm');
    let seconds = this.datePipe.transform(date, 'ss');
    return `${hours}:${minutes} ${seconds}s`;
  }

  drawGauge() {
    let circlePath = document.getElementsByClassName(
      'circle'
    )[0] as HTMLElement;
    this.percentage = this.actualCar.batteryLevel / 2;
    circlePath!.style.strokeDasharray = `${this.percentage}, 100`;
  }
}
