import { Component } from '@angular/core';

@Component({
  selector: 'propertybinding',
  standalone: true,
  imports: [],
  templateUrl: './propertybinding.component.html',
  styleUrl: './propertybinding.component.css'
})
export class PropertybindingComponent {
  email = 'vani@gmail.com';
  password = '';
}
