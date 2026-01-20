import { Component } from '@angular/core';

@Component({
  selector: 'stringintepolation',
  standalone: true,
  imports: [],
  templateUrl: './stringintepolation.component.html',
  styleUrl: './stringintepolation.component.css'
})
export class StringintepolationComponent {
  title:string="Products";
  product={
    name:"Lenovo Laptop",
    price:999,
    discount:8.5,
    color:"black"
  };
  getDiscount(){
    return this.product.price - (this.product.discount*this.product.price/100)
  }
}
