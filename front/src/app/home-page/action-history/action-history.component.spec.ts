import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActionHistoryComponent } from './action-history.component';

describe('ActionHistoryComponent', () => {
  let component: ActionHistoryComponent;
  let fixture: ComponentFixture<ActionHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ActionHistoryComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ActionHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
