import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { LoginFormComponent } from './login-form/login-form.component';
import { NestedformComponent } from './nestedform/nestedform.component';
import { StringintepolationComponent } from './stringintepolation/stringintepolation.component';
import { PropertybindingComponent } from './propertybinding/propertybinding.component';
import { EventbindingComponent } from './eventbinding/eventbinding.component';
import { TwowaydatabindingComponent } from './twowaydatabinding/twowaydatabinding.component';
import { StaticpageComponent } from './staticpage/staticpage.component';
import { MobileValidatorComponent } from './mobile-validator/mobile-validator.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ReactiveFormsModule, FormsModule, LoginFormComponent,
             NestedformComponent, StringintepolationComponent, PropertybindingComponent,
              EventbindingComponent,TwowaydatabindingComponent,StaticpageComponent,MobileValidatorComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Forms-app';
}
