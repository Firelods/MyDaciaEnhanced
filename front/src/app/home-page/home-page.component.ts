import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';
import { FooterComponent } from '../footer/footer.component';
import { CarInfoService } from '../services/car-info.service';
import { CarInfo } from '../interfaces/car-info';
@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [CommonModule, FooterComponent],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.scss',
})
export class HomePageComponent implements AfterViewInit {
  actualCar: CarInfo;
  percentage = 65;
  @ViewChild('circlePath')
  circlePath!: ElementRef;

  constructor(
    private carInfoService: CarInfoService,
    private datePipe: DatePipe
  ) {
    this.actualCar = this.carInfoService.getCarInfo();
  }



  ngAfterViewInit() {
    this.drawGauge();
  }

  formatDate(date: Date): string {
    let hours = this.datePipe.transform(date, 'HH');
    let minutes = this.datePipe.transform(date, 'mm');
    let seconds = this.datePipe.transform(date, 'ss');
    return `${hours}:${minutes} ${seconds}s`;
  }

  drawGauge() {
    // make pourcentage between 0 and 50
    this.percentage = this.percentage / 2;
    this.circlePath.nativeElement.style.strokeDasharray = `${this.percentage}, 100`;
  }
}
