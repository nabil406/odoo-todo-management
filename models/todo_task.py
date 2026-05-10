

from odoo import models, fields



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
    ], string="Status", default='new' , tracking=True)

    user_id= fields.Many2one('res.users' , string='Assigned To')  # to assign the task to a specific user from res.users model

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
