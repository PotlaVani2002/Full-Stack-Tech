import { Component } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-nestedform',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './nestedform.component.html',
  styleUrl: './nestedform.component.css'
})
export class NestedformComponent {

 userForms: FormGroup = new FormGroup({
    name: new FormControl(''),
    age: new FormControl(0),
    address: new FormGroup({
      ad1: new FormControl(''),
      ad2: new FormControl(''),
      city: new FormControl(''),
      state: new FormControl('')
    })
  });

  saveUser() {
    console.log(this.userForms.value);
  }
}
