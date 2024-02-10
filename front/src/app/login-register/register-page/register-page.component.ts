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
  phase: string = 'credentials';
  availableVehicles: VehicleList[] = [];
  constructor(private userService: UserService) {}

  submit() {
    console.log(this.form.value);

    this.userService.login(this.form.value.email, this.form.value.password);
  }
}
