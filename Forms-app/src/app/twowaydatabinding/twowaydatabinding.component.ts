import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
@Component({
  selector: 'twowaydatabinding',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './twowaydatabinding.component.html',
  // styleUrl: './twowaydatabinding.component.css'
})
export class TwowaydatabindingComponent {
    Username:string='';
}
