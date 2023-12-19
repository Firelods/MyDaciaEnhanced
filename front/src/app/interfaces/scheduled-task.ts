export interface ScheduledTask {
  timestamp: Date;
  task: string;
  type: string;
  success: boolean;
}
