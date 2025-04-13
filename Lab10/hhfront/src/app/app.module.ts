import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Компоненты
import { AppComponent } from './app.component';  // Импортировать вместо добавления в declarations
import { AddVacancyComponent } from './components/add-vacancy/add-vacancy.component';
import { CompanyDetailsComponent } from './components/company-details/company-details.component';
import { CompanyListComponent } from './components/company-list/company-list.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { VacancyDetailsComponent } from './components/vacancy-details/vacancy-details.component';
import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';

@NgModule({
  declarations: [
    CompanyListComponent,
    VacancyListComponent,
    HomePageComponent,
    CompanyDetailsComponent,
    VacancyDetailsComponent,
    AddVacancyComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    AppComponent,  // Добавьте AppComponent сюда
    CompanyListComponent,
    VacancyListComponent,
    HomePageComponent,
    CompanyDetailsComponent,
    VacancyDetailsComponent,
    AddVacancyComponent
  ],
  providers: [],
})
export class AppModule { }
