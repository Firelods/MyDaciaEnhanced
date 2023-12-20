import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CarInfoService {

  constructor() { }

  getCarInfo() {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    return {
      id: 1,
      name: 'Spring',
      autonomy: 151,
      imageUrl: 'https://www.tesla.com/sites/default/files/modelsx-new/social/model-s-hero-social.jpg',
      charging: true,
      climate: false,
      lastRefresh: new Date(),
      totalKilometers: 658,
      batteryLevel: 65,
      scheduled: {
        airConditioning: {
          timestamp: tomorrow,
          enabled: true
        },
        charging: {
          timestamp: yesterday,
          enabled: false
        }
      }
    };
  }

}
