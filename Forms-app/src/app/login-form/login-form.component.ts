import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login-form.component.html',
  styleUrl: './login-form.component.css'
})
export class LoginFormComponent {

  userForms:FormGroup=new FormGroup({
    age:new FormControl('0'),
    name:new FormControl(''),
    address: new FormGroup({
      ad1:new FormControl(''),
      ad2:new FormControl(''),
      state:new FormControl(''),
      city:new FormControl(''),
    })

  })
  
  saveUser(){
    // debugger;
    const obj=this.userForms.value;
    console.log(obj)
  }
}
