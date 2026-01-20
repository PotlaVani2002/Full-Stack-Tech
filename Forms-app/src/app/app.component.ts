import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { LoginFormComponent } from './login-form/login-form.component';
import { NestedformComponent } from './nestedform/nestedform.component';
import { StringintepolationComponent } from './stringintepolation/stringintepolation.component';
import { PropertybindingComponent } from './propertybinding/propertybinding.component';
import { EventbindingComponent } from './eventbinding/eventbinding.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,ReactiveFormsModule,FormsModule,LoginFormComponent,NestedformComponent,StringintepolationComponent,PropertybindingComponent,EventbindingComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Forms-app';
}
