import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
  HttpRequest,
} from '@angular/common/http';
// import {Observable} from 'rxjs/Observable';
import { API_URL } from '../env';
import { Measurement } from './measurement.model';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Injectable()
export class MeasurementApiService {
  constructor(private httpClient: HttpClient) {}

  /**
   * Gets all the blood measurements from the database
   *
   * @type {Observable<Measurement[]>}
   * @memberof MeasurementApiService
   */
  getMeasurements(): Observable<Measurement[]> {
    let headers: HttpHeaders = new HttpHeaders();
    headers = headers.append('Accept', 'application/json');
    return this.httpClient
      .get(`${API_URL}/measurements`, { headers: headers })
      .pipe(
        map((data: Measurement[]) => {
          return data;
        }),
        catchError((error) => {
          return throwError('Capital not found!');
        })
      );
  }
}
