import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true  // Убедитесь, что этот флаг добавлен
})
export class AppComponent {
  title = 'My Angular App';
}
