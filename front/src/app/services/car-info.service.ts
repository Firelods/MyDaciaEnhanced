import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CarInfoService {

  constructor() { }

  getCarInfo() {
    return {
      id: 1,
      name: 'Spring',
      autonomy: 151,
      imageUrl: 'https://www.tesla.com/sites/default/files/modelsx-new/social/model-s-hero-social.jpg',
      charging: false,
      climate: false,
      lastRefresh: new Date(),
      totalKilometers: 658,
      batteryLevel: 65
    };
  }

}
