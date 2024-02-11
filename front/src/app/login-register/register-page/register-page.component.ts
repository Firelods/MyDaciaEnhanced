import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { UserService } from '../../services/user.service';
import { FooterComponent } from '../../footer/footer.component';
import { VehicleList } from '../../interfaces/vehicle-list';

@Component({
  selector: 'app-register-page',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, FooterComponent],
  templateUrl: './register-page.component.html',
  styleUrl: './register-page.component.scss',
})
export class RegisterPageComponent {
  form: FormGroup = new FormGroup({
    email: new FormControl(''),
    password: new FormControl(''),
  });
  phase: string = 'chooseVehicle'; //  'credentials';
  availableVehicles: VehicleList[] = [];
  selectedVehicle: VehicleList | null = null;
  constructor(private userService: UserService) {
    this.userService
      .init_renault_login(this.form.value.email, this.form.value.password)
      .subscribe((vehicles) => {
        this.availableVehicles = vehicles;
        this.phase = 'chooseVehicle';
      });
  }

  submit() {
    this.userService
      .init_renault_login(this.form.value.email, this.form.value.password)
      .subscribe((vehicles) => {
        this.availableVehicles = vehicles;
        this.phase = 'chooseVehicle';
      });
  }

  chooseVehicle() {
    if (!this.selectedVehicle) {
      return;
    }
    this.userService.chooseVehicle(this.selectedVehicle.vin);
  }

  selectVehicle(vehicle: VehicleList) {
    if (this.selectedVehicle === vehicle) {
      this.selectedVehicle = null;
      return;
    }
    this.selectedVehicle = vehicle;
  }
}
