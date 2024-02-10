import { Component } from '@angular/core';

import { FooterComponent } from '../../footer/footer.component';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [FooterComponent, FormsModule, ReactiveFormsModule],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.scss',
})
export class LoginPageComponent {
  form: FormGroup = new FormGroup({
    email: new FormControl(''),
    password: new FormControl(''),
  });

  constructor(private userService: UserService) {}

  submit() {
    console.log(this.form.value);

    this.userService.login(this.form.value.email, this.form.value.password);
  }
}
