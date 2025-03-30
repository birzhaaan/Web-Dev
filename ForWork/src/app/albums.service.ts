import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  private baseUrl = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient) {}

  getAlbums(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/albums`);
  }

  getAlbum(id: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/albums/${id}`);
  }

  getPhotos(id: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/albums/${id}/photos`);
  }

  deleteAlbum(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/albums/${id}`);
  }

  updateAlbum(id: number, title: string): Observable<any> {
    return this.http.put(`${this.baseUrl}/albums/${id}`, { title });
  }
}
