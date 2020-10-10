/**
 * Measurement class with measurement fields
 * 
 * @export
 * @class Measurement
 */
export class Measurement {
    constructor(
      public title: string,
      public description: string,
      public systolic: number,
      public diastolic: number,
      public pulse: number,
      public _id?: number,
      public updatedAt?: Date,
      public createdAt?: Date,
      public lastUpdatedBy?: string,
    ) { }
  }