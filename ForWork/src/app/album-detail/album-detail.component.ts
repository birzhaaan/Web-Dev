import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: any;

  constructor(
    private albumsService: AlbumsService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    const id = +this.route.snapshot.paramMap.get('id')!;
    this.albumsService.getAlbum(id).subscribe(data => {
      this.album = data;
    });
  }

  saveChanges() {
    const id = this.album.id;
    const title = this.album.title;
    this.albumsService.updateAlbum(id, title).subscribe();
  }

  goBack() {
    this.router.navigate(['/albums']);
  }
}
