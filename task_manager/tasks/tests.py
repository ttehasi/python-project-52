from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password'
        )
        self.client.login(
            username='user',
            password='password'
        )
        self.status = Status.objects.create(name='status')
        self.status2 = Status.objects.create(name='status2')
        self.task = Task.objects.create(
            name='task',
            creator=self.user,
            status=self.status,
            executor=self.user,
        )
        self.task2 = Task.objects.create(
            name='task2',
            creator=self.user2,
            status=self.status2,
            executor=self.user2,
        )

        self.task3 = Task.objects.create(
            name='task3',
            creator=self.user,
            status=self.status2,
            executor=self.user2,
        )
        
    def test_update_task(self):
        data = {
            "name": "taskno1",
            "description": "description",
            "status": self.status.id,
        }

        response = self.client.post(
            reverse('task_update', args=[self.task.id]), data
        )

        self.assertEqual(response.status_code, 302)

        new_task = Task.objects.get(pk=self.task.id)
        self.assertEqual(new_task.name, data['name'])
        self.assertEqual(new_task.description, data['description'])
        
    def test_task_delete(self):
        response = self.client.post(
            reverse('task_delete', args=[self.task3.id]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
        
        response = self.client.post(
            reverse('task_delete', args=[self.task2.id]))
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
