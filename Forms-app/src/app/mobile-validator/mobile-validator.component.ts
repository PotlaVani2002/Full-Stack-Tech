import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AbstractControl,FormControl,FormGroup,ReactiveFormsModule,Validators,ValidationErrors } from '@angular/forms';

@Component({
  selector: 'app-mobile-validator',
  standalone: true,
  imports: [ReactiveFormsModule,CommonModule],
  templateUrl: './mobile-validator.component.html',
})
export class MobileValidatorComponent {

  mobileForm = new FormGroup({
    mobile: new FormControl('', [
      Validators.required,
      this.mobileValidator
    ])
  });

  mobileValidator(control: AbstractControl): ValidationErrors | null {
    const value = control.value;
    if (!value) {
      return null; // required will handle empty case
    }

    const pattern = /^[6-9][0-9]{9}$/;

    return pattern.test(value)
      ? null
      : { mobileInvalid: true };
  }

  show(){
    console.log(this.mobileForm);
    alert("Thank you")
  }
}
