from odoo import models, fields , api
from odoo.exceptions import ValidationError

class ToDo(models.Model):
    _name = 'todo.task'
    _description = 'Task Record'  # to appear for end user (Display name for user )
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True , string="Task Name" , tracking=True)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date" , tracking=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], string="Status", default='new' , tracking=True)

    user_id= fields.Many2one('res.partner' , string='Assigned To')  # to assign the task to a specific user from res.partner model (Many2one relationship)

    # workflow methods
    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

    def action_closed(self):
        for rec in self:  # لازم Loop عشان التنفيذ الجماعي (Multi Records)
            rec.state = 'closed'

    estimated_time = fields.Float(string="Estimated Time (Hours)")
    line_ids = fields.One2many('todo.task.line', 'task_id', string="Timesheets")
    total_time = fields.Float(string="Total Time", compute='_compute_total_time', store=True)

    active = fields.Boolean(string="Active", default=True)
    is_late = fields.Boolean(string="Is Late", default=False)


    @api.depends('line_ids.time')
    def _compute_total_time(self):
        for rec in self:
            rec.total_time = sum(line.time for line in rec.line_ids)
            # rec.total_time = sum(rec.line_ids.mapped('time'))

    @api.constrains('total_time', 'estimated_time')
    def _check_total_time(self):
        for rec in self:
            if rec.estimated_time > 0 and rec.total_time > rec.estimated_time:
                raise ValidationError("Total time spent on the task cannot exceed the estimated time.")

    # def check_late_tasks(self):
    #     task_ids = self.search([])
    #     for rec in task_ids:
    #         if rec.due_date and rec.state != 'completed' and rec.due_date < fields.Date.today():
    #             rec.is_late = True
    #         else:
    #             rec.is_late = False

    # cron job method to check for late tasks
    def check_late_tasks(self):
        today = fields.Date.today()

        # 1. جلب كل المهام غير المكتملة وتاريخ استحقاقها فات
        late_tasks = self.search([
            ('due_date', '!=', False),
            ('due_date', '<', today),
            ('state', '!=', ['completed','closed']),
        ])
        late_tasks.write({'is_late': True})  #  تحديث حالة المهام المتأخرة إلى True

        # 2. إرجاع المهام التي لم يحن موعدها بعد إلى الحالة الطبيعية
        not_late_tasks = self.search([
            ('due_date', '>=', today),
        ])
        not_late_tasks.write({'is_late': False})


class TodoTaskLine(models.Model):
    _name = 'todo.task.line'
    _description = 'Task Timesheet Line'

    task_id = fields.Many2one('todo.task', string="Task", ondelete='cascade')
    date = fields.Date(string="Date", default=fields.Date.today, required=True)
    description = fields.Char(string="Description", required=True)
    time = fields.Float(string="Time (Hours)", required=True)