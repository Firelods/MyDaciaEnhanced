export interface CarInfo {
  id: number;
  name: string;
  autonomy: number;
  imageUrl: string;
  charging: boolean;
  climate: boolean;
  lastRefresh: Date;
  totalKilometers: number;
  batteryLevel: number;
}
