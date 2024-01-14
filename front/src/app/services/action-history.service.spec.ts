import { TestBed } from '@angular/core/testing';

import { ActionHistoryService } from './action-history.service';

describe('ActionHistoryService', () => {
  let service: ActionHistoryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ActionHistoryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
