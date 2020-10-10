import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { MeasurementApiService } from './measurements/measurement-api.service';
import { Measurement } from './measurements/measurement.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'measurements';
  measurementListSubs: Subscription;
  measurementList: Measurement[];

  constructor(private measurementApi: MeasurementApiService) {}

  ngOnInit() {
    this.measurementListSubs = this.measurementApi
      .getMeasurements()
      .subscribe((res) => {
        this.measurementList = res;
      }, console.error);
  }

  ngOnDestroy() {
    this.measurementListSubs.unsubscribe();
  }
}
