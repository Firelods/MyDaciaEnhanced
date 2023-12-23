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
export class HomePageComponent implements AfterViewInit {
  actualCar!: CarInfo;
  history: taskHistory[] = [];
  percentage = 65;
  @ViewChild('circlePath')
  circlePath!: ElementRef;
  viewInitialized = new Promise<void>(
    (resolve) => (this._resolveViewInitialized = resolve)
  );

  private _resolveViewInitialized!: () => void;
  constructor(
    private carInfoService: CarInfoService,
    private datePipe: DatePipe,
    private ActionHistoryService: ActionHistoryService
  ) {
    this.carInfoService.getCarInfo().subscribe((carInfo) => {
      this.actualCar = carInfo;
      this.viewInitialized.then(() => this.drawGauge());
    });
    this.history = this.ActionHistoryService.getHistory();
  }

  ngAfterViewInit() {
    this._resolveViewInitialized();
  }

  formatDate(date: Date): string {
    let hours = this.datePipe.transform(date, 'HH');
    let minutes = this.datePipe.transform(date, 'mm');
    let seconds = this.datePipe.transform(date, 'ss');
    return `${hours}:${minutes} ${seconds}s`;
  }

  drawGauge() {
    // make pourcentage between 0 and 50
    console.log(this.actualCar);
    this.actualCar.autonomy = 65;
    this.percentage = this.actualCar.autonomy / 2;
    this.circlePath.nativeElement.style.strokeDasharray = `${this.percentage}, 100`;
    console.log(this.circlePath);
  }
}
