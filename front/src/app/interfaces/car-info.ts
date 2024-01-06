import { taskHistory } from './task-history';
import { ScheduledTask } from './scheduled-task';

export interface CarInfo {
  name: string;
  autonomy: number;
  imageUrl: string;
  charging: boolean;
  climate: boolean;
  lastRefresh: Date;
  totalKilometers: number;
  batteryLevel: number;
  scheduled: {
    airConditioning: ScheduledTask;
    charging: ScheduledTask;
  };
  history: taskHistory[];
}
