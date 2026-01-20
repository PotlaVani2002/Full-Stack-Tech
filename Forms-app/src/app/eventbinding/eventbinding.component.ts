import { Component } from '@angular/core';

@Component({
  selector: 'eventbinding',
  standalone: true,
  imports: [],
  templateUrl: './eventbinding.component.html',
  // styleUrl: './eventbinding.component.css'
})
export class EventbindingComponent {
  email:string='';
  onEmailChange(event:any){
    this.email=event.target.value;
  }
}
